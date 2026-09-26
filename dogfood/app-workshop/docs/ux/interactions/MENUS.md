# Menus, commands, and menu bar

There are different kinds of “menu.” Choose the surface from the user's task, not from a desire to hide controls.

| Surface | Typical use | Native starting point |
| --- | --- | --- |
| In-view menu | Related choices from a visible control | SwiftUI `Menu` |
| Context menu | A small set of actions for a specific item | `contextMenu` |
| Mac and iPad menu bar | App-wide commands, editing, windows, and shortcuts | Scene `.commands`, `CommandMenu`, `CommandGroup` |
| Mac status item | A persistent menu bar presence only when the product needs it | `MenuBarExtra` |
| iPhone navigation or toolbar | Frequent screen actions | `ToolbarItem`, `Button`, `Menu` as needed |

## Command rules

- Keep the same command name and outcome across toolbar, context menu, menu bar, and keyboard shortcut.
- Put common actions where they are visible; a long-press-only or context-menu-only action is easy to miss.
- Let the system supply standard edit and window commands. Add app-specific commands to appropriate groups and avoid shortcut conflicts.
- Enable a command only when it can work for the current selection or focused window. If it cannot, preserve the expected disabled state.
- Use separators and submenus to group related actions; avoid deep nesting for a tiny command set.
- A Mac menu bar is part of a normal Mac app. A `MenuBarExtra` is a separate status-item experience and should be optional, not a replacement for the app's commands.

**Dogfood path:** execute each command from the visible control, menu bar, context menu, and shortcut where those surfaces exist. Verify all paths produce the same result and error behavior. Then test with multiple windows and changed focus.

Apple references: [Menus HIG](https://developer.apple.com/design/human-interface-guidelines/menus), [Menus and commands](https://developer.apple.com/documentation/swiftui/menus-and-commands), [Building and customizing the menu bar with SwiftUI](https://developer.apple.com/documentation/swiftui/building-and-customizing-the-menu-bar-with-swiftui). Reviewed 2026-09-25.
