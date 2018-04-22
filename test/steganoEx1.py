def decode_img(file_loc= "data/encoded_sample.png"):
    encoded_img= Image.open(file_loc)
    red_channel= encoded_img.split()[0]
    return red_channel
print(decode_img())
