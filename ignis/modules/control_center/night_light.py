from .qs_button import QSButton
import subprocess

def night_light_button() -> QSButton:
    # State variable to track if night light is active
    is_active = False

    def activate_night_light():
        nonlocal is_active
        if not is_active:
            subprocess.run(["bash", "-c", "hyprshade on blue-light-filter"], check=True)  # Command to enable Night Light
            is_active = True  # Update state
            update_button_state()  # Update the button state

    def deactivate_night_light():
        nonlocal is_active
        if is_active:
            subprocess.run(["bash", "-c", "hyprshade toggle blue-light-filter"], check=True)  # Command to disable Night Light
            is_active = False  # Update state
            update_button_state()  # Update the button state

    def update_button_state():
        """Update the button's visual state."""
        if is_active:
            button.label = "Night Light:On"
        else:
            button.label = "Night Light:Off"
          # Change to the inactive icon
        button.active = is_active  # Update the button's active state

    # Create the QSButton instance
    button = QSButton(
        label="Night Light",
        icon_name="night-light-disabled-symbolic",  # Initial icon
        on_activate=lambda x: activate_night_light(),
        on_deactivate=lambda x: deactivate_night_light(),
        active=is_active  # Set the default state
    )

    return button
