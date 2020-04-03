import Services
import Repositories
import config
from flask_restx import Resource, Api
from flask import Flask

app = Flask(__name__)
api = Api(app)


@api.route('/get_word_count/<int:threshold>')
class MainClass(Resource):
    def get(self, threshold):
        scanner = Services.DirectoryScanner(config.DIRECTORIES_TO_SCAN)
        interesting_service = Services.InterestingService(config.DEFAULT_INTERESTING_WEIGHT)
        document_parser = Services.DocumentParser()
        repo = Repositories.TxtRepository()
        counting_service = Services.WordCountingService(document_parser, interesting_service, threshold)

        for file in scanner.scan_files():
            for line in repo.read_file(file):
                for sentence in document_parser.split_to_sentences(line):
                    counting_service.populate(sentence, file)

        return counting_service.get_word_count()


if __name__ == '__main__':
    app.config.from_object('config')
    app.run(port=config.PORT_NUMBER)


