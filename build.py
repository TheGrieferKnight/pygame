import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["assets/", "main_game.py", "bullet.py", "sprites.py", "enemy.py", "player.py", "settings.py", "waves.py"]}},
    executables = executables

    )