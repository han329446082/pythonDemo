import MySQLdb
import pytest
uatconn = MySQLdb.connect(
    user = 'root',
    passwd = 'yami@123',
    host = 'uat-k8s-cluster.cluster-c5ywutgewymm.us-west-2.rds.amazonaws.com',
    port = 3306,
    db = 'yamibuy_sns',
    charset = 'utf8'
)

def get_data():
    query_sql = 'select rec_id,title from `yamibuy_sns`.`live_activity`  order by 1 desc LIMIT 10; '
    lst = []
    try:
        cursor = uatconn.cursor()
        cursor.execute(query_sql)
        r = cursor.fetchall()
        for x in r:
            u = (x[0],x[1])
            lst.append(u)
        return lst
    finally:
        cursor.close()
        uatconn.close()

@pytest.mark.parametrize('data',get_data())
def test01(data):
    print(data)

if __name__ == '__main__':
    pytest.main(['-sv','test_db.py'])