import logic2
import utils
import arg_init

if __name__ == "__main__":
    arg_parser = arg_init.init_arg_parser()
    args = arg_parser.parse_args()
    # if len(sys.argv) < 2:
    #     print("Data file not defined by argv.")
    #     exit(1)
    word_size = args.size
    if not word_size:
        word_size = int(input("Enter word size :"))

    try:
        words = utils.load_data(args.input)
    except Exception as e:
        print("Data load error : " + str(e))
        exit(2)

    if word_size < 1:
        print("Invalid word size parameter")
        exit(3)

    try:
        processed = logic2.select_words(size=word_size, data=words)
        # processor = logic2.unique_words(logic2.select_words)
        # processed = processor(words, word_size)
    except Exception as e:
        print("Data processing error : " + str(e))
        exit(4)

    if len(processed) == 0:
        print("Not found")
        exit(5)
    print(processed)
    utils.save_data(args.output, processed)


