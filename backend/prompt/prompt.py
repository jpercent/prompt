import datetime
import difflib
import flask
#import flask.ext.cors
import json
import logging
import mysql.connector
import traceback

__author__ = 'jpercent'

application = flask.Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FiveHundred(Exception):
    pass


class Database(object):
    def __init__(self, user='james', password='james', host='127.0.0.1', database='conversations',
                 raise_on_warnings=True):
        self.conf=\
        {
            'user': user,
            'password': password,
            'host': host,
            'database': database,
            'raise_on_warnings': raise_on_warnings,
        }
    def get_conn(self):
        try:
            cnx = mysql.connector.connect(**self.conf)
            return cnx
        except Exception as e:
            logger.error(traceback.format_exc())
            raise Exception(e)


def curate_deltas(conf):
    try:
        assert conf and 'mysql' in conf
        deltas_query = \
        """
            SELECT question_id, version, question
            FROM conversations.questions q
            ORDER BY q.question_id, q.version ASC
        """
        db = Database(**conf['mysql'])
        cnx = db.get_conn()
        cursor = cnx.cursor()
        cursor.execute(deltas_query)
        results = cursor.fetchall()
        new_question = True
        curated_results = []
        for i in range(len(results)):
            if i+1 != len(results):
                if results[i][0] == results[i+1][0]:
                    version_diff = list(difflib.ndiff(results[i][2].split(),results[i+1][2].split()))
                    curated_results.append(version_diff)
                    diff_sep = '-'*80
                    curated_results.append([diff_sep,])
        cursor.close()
        cnx.close()
        return curated_results
    except Exception as e:
        logger.error(traceback.format_exc())
        raise FiveHundred(e)


@application.route("/deltas", methods=['GET', 'OPTIONS'])
def get_deltas():
    if flask.request.method == 'OPTIONS':
        response = flask.Response(response=json.dumps({'resp': 'OK'}), status=200, mimetype="application/json")
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, PATCH, DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,content-type'
        return response
    else:
        deltas = curate_deltas(application.conf)
        response = flask.Response(response=json.dumps({'deltas': deltas}), status=200, mimetype="application/json")
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, PATCH, DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,content-type'
        return response

def print_deltas(conf):
    deltas = curate_deltas(conf)
    for delta in deltas:
        print(delta)


@application.route("/sentence", methods=['POST','OPTIONS'])
def post_sentence():
    if flask.request.method == 'OPTIONS':
        response = flask.Response(response=json.dumps({'resp': 'OK'}), status=200, mimetype="application/json")
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, PATCH, DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,content-type'
        return response

    response = None
    try:
        insert_sentence(json.loads(flask.request.data)['question'], application.conf)
    except:
        response = flask.Response(response=json.dumps({'resp': 'BAD'}), status=400, mimetype="application/json")

    if not response:
        response = flask.Response(response=json.dumps({'resp': 'OK'}), status=200, mimetype="application/json")
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, PATCH, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,content-type'
    return response


def insert_sentence(sentence, conf):
    try:
        insert_sentence_stmt = \
        """
        INSERT INTO conversations.questions
        SELECT max(question_id)+1, 0, \'{}\'
        FROM conversations.questions
        """.format(sentence)
        db = Database(**conf['mysql'])
        cnx = db.get_conn()
        cursor = cnx.cursor()
        cursor.execute(insert_sentence_stmt)
        cursor.close()
        cnx.commit()
        cnx.close()
    except Exception as e:
        logger.error(traceback.format_exc())
        raise FiveHundred(e)


def launch_app(conf_file_path='local.json'):
    conf = None
    with open(conf_file_path) as f:
        conf = json.loads(f.read())

    application.conf = conf
    application.secret_key = conf['secret_key']
    return application


if __name__ == "__main__":
    application = launch_app()
    application.run(port=8083)
