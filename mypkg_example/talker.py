import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）
from person_msgs_example.msg import Person   #変更: 作ったPerson型を使う

rclpy.init()                     #rclpyの初期化（最初に1回）
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
pub = node.create_publisher(Person, "person", 10)   #変更: 型とトピック名
n = 0                            #カウント用変数

def cb():               #タイマーで定期的に呼ばれるコールバック関数
    global n            #関数を抜けてもnがリセットされないようにしている
    msg = Person()          #変更: Person型のメッセージを作る
    msg.name = "鈴木太郎"    #変更: msgファイルに書いた「name」
    msg.age = n % 256       #変更: msgファイルに書いた「age」（0〜255まで）
    pub.publish(msg)    #pubの持つpublishでメッセージ送信（パブリッシュ）
    n += 1


def main():
    node.create_timer(0.5, cb)  #0.5秒ごとにcbを呼ぶタイマー
    rclpy.spin(node)            #実行（無限ループ。タイマーや送受信を処理し続ける）

