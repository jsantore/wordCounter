
def open_file(file_name):
    file = open(file_name,'r', encoding='utf-8')
    lines = file.readlines()
    return lines


def display_result(word_counts):
    for word in word_counts:
        count = word_counts[word]
        print(f"{word}:\t {count}")


def main():
    file_lines = open_file("warpeace.txt")
    word_counts = word_count(file_lines)
    display_result(word_counts)

def word_count(all_lines):
    word_counter = {}
    for line in all_lines:
        words_in_line = line.split(' ')
        for word in words_in_line:
            if word in word_counter:
                word_counter[word]+= 1
            else:
                word_counter[word] = 1
    return word_counter

main()