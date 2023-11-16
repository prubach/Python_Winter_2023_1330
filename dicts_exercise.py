my_text = 'In a competitive research environment, publishing is not enough anymore. You have to make your research accessible, findable and visible. Your online identity is the central key for your career and your recognition, particularly for young researchers. This session will help you to build your online research profile by applying best practices. You will learn how to evaluate your online identity and promote your work by using the tools best suited to your needs. A special focus on ORCID will be presented.'
# TODO:
# 1. delete special symbols (replace) ,.'
for sym in [',', '.', '"', '\'']:
    my_text = my_text.replace(sym, '')
print(my_text)
# 2. create a dictionary with keys representing words in the text and values the
# number of times they appear
my_word_list = my_text.split()
print(my_word_list)