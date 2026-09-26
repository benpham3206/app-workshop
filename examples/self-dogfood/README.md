# Self-dogfood selection

This selects the boilerplate's first real test product: a Mac-first beginner guide for taking an Apple app from idea to ongoing support. It is a learning prototype, not a released brand or a claim that every Apple platform is implemented.

The same `config/process.json` supplies the generated beginner guide and the native prototype. The app icon begins as generated concept art, then is refined with a circle construction grid and packaged as a Mac icon.

Regenerate into a new empty destination with `make generate CONFIG=examples/self-dogfood/project.json OUTPUT=dist/app-workshop`. The checked-in dogfood snapshot under `dogfood/app-workshop/` adds native app source and evidence; the generator deliberately refuses to overwrite it.
