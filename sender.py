# with open('source/Okay (Meme Sound) - Sound Effect for editing ( 256kbps cbr ).mp3', 'rb') as mp3_file:
#     binary_data = mp3_file.read()
#
# # print(binary_data)
#
# with open('destination/example_reassembled.mp3', 'wb') as mp3_file:
#     mp3_file.write(binary_data)

with open('source/SudokuOffline.exe', 'rb') as mp3_file:
    binary_data = mp3_file.read()

with open('destination/example_reassembled.exe', 'wb') as mp3_file:
    mp3_file.write(binary_data)
