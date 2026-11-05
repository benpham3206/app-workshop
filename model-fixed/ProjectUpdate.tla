--------------------------- MODULE ProjectUpdate ---------------------------
CONSTANTS Old, New, Edit
ASSUME Old # New /\ Old # Edit /\ New # Edit

VARIABLES templateHash, manifestHash, projectHash, pathKind, outsideHash,
          builderEdited, plan

vars == <<templateHash, manifestHash, projectHash, pathKind, outsideHash,
         builderEdited, plan>>

Init ==
    /\ templateHash = New
    /\ manifestHash = Old
    /\ projectHash = Old
    /\ pathKind = "regular"
    /\ outsideHash = Old
    /\ builderEdited = FALSE
    /\ plan = "ready"

BuilderRedirectsGeneratedPath ==
    /\ plan = "ready"
    /\ pathKind = "regular"
    /\ projectHash = manifestHash
    /\ ~builderEdited
    /\ pathKind' = "symlink"
    /\ UNCHANGED <<templateHash, manifestHash, projectHash, outsideHash,
                    builderEdited, plan>>

BuilderEditsGeneratedFile ==
    /\ plan = "ready"
    /\ pathKind = "regular"
    /\ ~builderEdited
    /\ projectHash' = Edit
    /\ builderEdited' = TRUE
    /\ UNCHANGED <<templateHash, manifestHash, pathKind, outsideHash, plan>>

\* tooling/scaffold.py:335-346
UpdaterPlansReplacement ==
    /\ plan = "ready"
    /\ pathKind = "regular"
    /\ projectHash = manifestHash
    /\ projectHash # templateHash
    /\ plan' = "update"
    /\ UNCHANGED <<templateHash, manifestHash, projectHash, pathKind,
                    outsideHash, builderEdited>>

\* tooling/scaffold.py:335-350
UpdaterReportsConflict ==
    /\ plan = "ready"
    /\ (pathKind = "symlink"
        \/ (projectHash # templateHash /\ manifestHash # projectHash))
    /\ plan' = "conflict"
    /\ UNCHANGED <<templateHash, manifestHash, projectHash, pathKind,
                    outsideHash, builderEdited>>

\* tooling/scaffold.py:356-362
UpdaterAppliesReplacement ==
    /\ plan = "update"
    /\ projectHash' = templateHash
    /\ UNCHANGED outsideHash
    /\ manifestHash' = templateHash
    /\ plan' = "applied"
    /\ UNCHANGED <<templateHash, pathKind, builderEdited>>

\* tooling/scaffold.py:362-363
UpdaterFinishesWithConflict ==
    /\ plan = "conflict"
    /\ plan' = "conflictDone"
    /\ UNCHANGED <<templateHash, manifestHash, projectHash, pathKind,
                    outsideHash, builderEdited>>

Done ==
    /\ plan \in {"applied", "conflictDone"}
    /\ UNCHANGED vars

Next == BuilderRedirectsGeneratedPath
     \/ BuilderEditsGeneratedFile
     \/ UpdaterPlansReplacement
     \/ UpdaterReportsConflict
     \/ UpdaterAppliesReplacement
     \/ UpdaterFinishesWithConflict
     \/ Done

BuilderEditsSurvive ==
    builderEdited => (pathKind = "regular" /\ projectHash = Edit)

OutsideProjectFileIsUntouched == outsideHash = Old

Spec == Init /\ [][Next]_vars
=============================================================================
