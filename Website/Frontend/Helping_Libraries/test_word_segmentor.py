import word_segmentor

segmentor = word_segmentor.load_word_segmentor(data_path='./data/all_vocal_books.txt')

print(segmentor.segment('mynameisbhumitadivarekar'))