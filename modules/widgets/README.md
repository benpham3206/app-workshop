# Widgets module

Use when a product has useful glanceable or quick-action content outside its app. A widget uses WidgetKit timelines and rendering modes. A Live Activity uses ActivityKit updates and has its own lifecycle; selecting one does not automatically select the other.

WidgetKit surfaces span iPhone, iPad, Mac, Apple Watch, and Apple Vision Pro. A tvOS-only project cannot select this module; add a supported host platform before planning a widget.

Before implementation, specify each widget family, update source and cadence, tap destination, privacy redaction, appearance variants, and accessibility labels. Add a watchOS app and widget extension when offering native Watch widgets or complications.

Source checked 2026-09-25: [WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy/), [additional appearances](https://developer.apple.com/documentation/widgetkit/preparing-widgets-for-additional-contexts-and-appearances).
