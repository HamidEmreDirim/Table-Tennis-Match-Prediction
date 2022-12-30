from tkinter import *
from tkinter import filedialog
from PIL import Image

watermark_image = ""
watermark_image_id_list = []
original_image = ""
original_image_id_list = []
watermark_tag = False
image_tag = False
watermark_label_contents = ''
image_label_contents = ''
show_image = 0


im1 = ""
im2 = ""
num = "20"
alpha_val = int(num) / 100


def choose_image():
    global original_image, image_tag, watermark_tag, \
        image_label_contents, watermark_label_contents, \
        im1, original_image_id_list

    watermark_tag = True
    original_image = filedialog.askopenfilename(initialdir='../',
                                                title='Select an image.',
                                                filetypes=[("Image files", "*.jpg *.png")])
    im1 = Image.open(original_image)
    original_image_id_list = original_image.split(".")

    # Change label contents
    image_label_contents = f"Image Opened: {original_image}"
    if watermark_tag == True:
        label_file_explorer.configure(text=f"{watermark_label_contents}\n{image_label_contents}")
    else:
        label_file_explorer.configure(text=image_label_contents)
    # im1.show()


def choose_watermark():
    global watermark_image, image_tag, watermark_tag, image_label_contents, watermark_label_contents, im2, watermark_image_id_list
    watermark_image = filedialog.askopenfilename(initialdir='../',
                                                 title='Select a watermark.',
                                                 filetypes=[("Image files", "*.jpg *.png")])
    im2 = Image.open(watermark_image)
    watermark_image_id_list = original_image.split(".")
    # Change label contents
    watermark_label_contents = f"Watermark Opened: {watermark_image}"
    if image_tag == True:
        label_file_explorer.configure(text=f"{watermark_label_contents}\n{image_label_contents}")
    else:
        label_file_explorer.configure(text=watermark_label_contents)
    # im2.show()


def update_scale(value_from_scale):
    global num
    num = value_from_scale
    scale_label.configure(text=f"Strength of Watermark:\n{num}")


def apply_watermark():
    # getbox() gets the dimensions of the picture so that the watermark can be resized to match it.
    global im1, im2, watermark_label_contents
    box = im1.getbbox()
    im2 = im2.resize(size=(box[2], box[3]))
    # Apply the watermark
    try:
        im1 = Image.blend(im1, im2, alpha=alpha_val)
    except ValueError:
        label_file_explorer.configure(text="The file types of the watermark and the image must be the same\(.jpg or .png\)")
    else:
        im1.save(f"{original_image_id_list[0]}_WM.{original_image_id_list[1]}")
        label_file_explorer.configure(text=f"{watermark_label_contents}\nSuccess! ")
        print(show_image)
        if show_image % 2 != 0:
            im1.show()

def check_box():
    global show_image
    show_image +=1


# Create the root window
window = Tk()
window.title("Alan's Watermarker")
window.geometry('600x500+200+0')
window.config(background="#d793ff")


# Create the buttons, labels, etc. for the TkInter window
# checkbutton = Checkbutton(window, variable=show_image, onvalue=1, offvalue=0, highlightthickness=0,fg="blue", bg="#d793ff")
checkbutton = Checkbutton(window, highlightthickness=0,fg="blue", bg="#d793ff", command=check_box)

label_file_explorer = Label(window,
                            text="This application accepets .jpg or .png type files. Both files must be "
                                 "of the same type \n\nWatermark not chosen\n\nImage not chosen",
                            # width=100, height=4,
                            fg="blue", bg="#d793ff", pady=15, font=('arial', 14))


button_watermark = Button(window,
                          text="Choose an image for the watermark",
                          command=choose_watermark, fg='#a193ff', highlightthickness=0, padx=20, pady=10)


button_exit = Button(window,
                     text="Exit", highlightthickness=0, fg='#a193ff', padx=20, pady=10,
                     command=exit)


button_image = Button(window,
                      text="Choose a file to mark", highlightthickness=0, fg='#a193ff',
                      command=choose_image, bg='green', padx=20, pady=10)


button_run = Button(window,
                    text="Apply Watermark", highlightthickness=0, fg='#a193ff', padx=20, pady=10,
                    command=apply_watermark)



scaler = Scale(window, orient=VERTICAL, from_=70.0, to=10.0, length=200, showvalue=False, command=update_scale)


scale_label = Label(window, text=f"Strength of Watermark:\n{num}", fg="blue", bg="#d793ff", font='bold')


# sets the default value for watermark strength
scaler.set(20)


# Grid positions
checkbutton.grid(column=0, row=3, sticky='w', padx=10,)
label_file_explorer.grid(column=0, row=0, padx=20, pady=20, columnspan=2)
button_watermark.grid(column=0, row=1, padx=20, pady=10)
button_image.grid(column=0, row=2, padx=20, pady=10)
button_exit.grid(column=0, row=4, padx=20, pady=10)
button_run.grid(column=0, row=3, padx=20, pady=10)
scaler.grid(column=1, row=2, rowspan=3, padx=20, pady=10)
scale_label.grid(column=1, row=1, sticky="s")


# Check to see if there is a default watermark already in the project
try:
    im2 = Image.open("default_watermark.jpg")
    watermark_image = 'default_watermark.jpg'
    watermark_label_contents = f"Watermark Opened: {watermark_image}"
    label_file_explorer.configure(text=f"This application accepets .jpg or .png type files. Both files must be "
                                 f"of the same type\n\nCheck the box to open the final watermarked image upon completion. \n\n{watermark_label_contents}\n\nImage not chosen")
except FileNotFoundError:
    try:
        im2 = Image.open("default_watermark.png")
        watermark_image = 'default_watermark.png'
        watermark_label_contents = f"Watermark Opened: {watermark_image}"
    except FileNotFoundError:
        pass

window.mainloop()
