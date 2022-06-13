from app import App


def start():
    app = App()
    app.initialize_app()
    app.configure_display()
    app.run()


if __name__ == "__main__":
    start()



