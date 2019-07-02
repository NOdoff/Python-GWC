import filters

def main():
    image = filters.load_img("super_nova.jpg")
    new_image = filters.obamicon(image)
    filters.show_img(new_image)

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
