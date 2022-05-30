import script_manager
def main():
    print("Hello World!")
    script = script_manager.Script()
    script.init()
    while True:
        script.update()
        script.draw()
    script.destroy()

if __name__ == "__main__":
    main()
