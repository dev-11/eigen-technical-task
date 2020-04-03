import sys
import Services
import Repositories
import config


def main():
    scanner = Services.DirectoryScanner(config.DIRECTORIES_TO_SCAN)
    interesting_service = Services.InterestingService(config.DEFAULT_INTERESTING_WEIGHT)
    document_parser = Services.DocumentParser()
    repo = Repositories.TxtRepository()
    counting_service = Services.WordCountingService(document_parser, interesting_service, config)

    for file in scanner.scan_files():
        text = repo.read_file(file)
        for line in text:
            sentences = document_parser.split_to_sentences(line)
            for sentence in sentences:
                counting_service.populate(sentence, file)

    lst = counting_service.get_word_count()
    print(*lst, sep="\n\n")


if __name__ == '__main__':
    sys.exit(main())

