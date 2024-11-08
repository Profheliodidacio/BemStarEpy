def navigate_to(screen_name, content_column, set_user_name=None, navigate_to=None):
    content_column.controls.clear()
    if screen_name == "info":
        from src.screens import info_tips_screen
        info_tips_screen.display(content_column)
    elif screen_name == "mental_health":
        from src.screens import mental_health_screen
        mental_health_screen.display(content_column)
    elif screen_name == "fun_area":
        from src.screens import fun_area_screen
        fun_area_screen.display(content_column)
    elif screen_name == "login":
        from src.screens import login_screen
        login_screen.display(content_column, set_user_name, navigate_to)
    elif screen_name == "about":
        from src.screens import about_screen
        about_screen.display(content_column)
    content_column.update()
