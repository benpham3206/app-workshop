export const title = "Generated project file update";

export const colors = {
  "Before update": "blue",
  "Update decision": "orange",
  "Result": "teal",
};

type StateVars = { plan: string; pathKind: string; builderEdited: boolean };

export const state = (v: StateVars) => {
  if (v.plan === "update") return "Replacement selected";
  if (v.plan === "conflict" || v.plan === "conflictDone") {
    return v.pathKind === "symlink" ? "Outside path rejected" : "Builder edit kept as conflict";
  }
  if (v.plan === "applied") return "Project file updated";
  if (v.pathKind === "symlink") return "Generated path points outside project";
  if (v.builderEdited) return "Builder edited generated file";
  return "Factory v2 available for a v1 project";
};

export const group = (v: StateVars) => {
  if (v.plan === "ready") return "Before update";
  if (v.plan === "update") return "Update decision";
  return "Result";
};

export const step = (action: string, from: StateVars) => {
  if (action === "UpdaterReportsConflict" && from.pathKind === "symlink") {
    return "updater rejects the outside path";
  }
  const labels: Record<string, string> = {
    BuilderRedirectsGeneratedPath: "generated path becomes a symlink",
    BuilderEditsGeneratedFile: "builder edits the generated file",
    UpdaterPlansReplacement: "updater selects the replacement",
    UpdaterReportsConflict: "updater keeps the builder edit",
    UpdaterAppliesReplacement: "updater copies the new template",
    UpdaterFinishesWithConflict: "updater leaves the conflict unchanged",
    Done: "update finishes",
  };
  return labels[action] ?? action;
};
