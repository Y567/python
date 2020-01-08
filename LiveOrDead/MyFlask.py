from flask import Flask, render_template, request

# 表示船上的人数
n = 0
# 表示离开船上的间隔人数
m = 0
# 最后船上的剩余人数
k = 0
# 活着的人数列表
live = []
# 死亡的人数列表
dead = []
# 存着所有人
people = {}


# 踢人下船的函数,i表示从哪个人开始
def kick(i):
    live_count = n
    # count 为统计的变量
    count = 1
    while live_count > k:
        if i == 0:
            # 避免除余运算得出0的情况
            i = i + 1
        if people[i] == 0:
            i = (i + 1) % (n + 1)
            continue
        if people[i] == 1:
            if count == m:
                people[i] = 0
                # print("{}号被众人仍在了海里，{}号大叫着救命！！！".format(index, index))
                # print(index)
                dead.append(i)
                live_count = live_count - 1
                # 因为要从下一个开始计时了，所以当前被人下海的人为0，从下一个开始从1开始计时
                count = 0
                # 存活人数减1
            count = (count + 1) % (m + 1)
        i = (i + 1) % (n + 1)


app = Flask(__name__)


# 设置路由
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/resolve", methods=['post'])
def fun():
    global n
    n = int(request.form.get("n"))
    global m
    m = int(request.form.get("m"))
    global k
    k = int(request.form.get("k"))
    begin = int(request.form.get("index"))

    print(n)
    print(m)
    print(k)
    print(begin)
    if n == 0 or m == 0 or k == 0 or begin == 0:
        return render_template("index.html")
    global live
    live = []
    global dead
    dead = []
    for i in range(n + 1):
        # 从一号开始先设置人全部为存活状态
        people[i + 1] = 1
    # 这里调用踢人下船函数来踢人
    kick(begin)
    for i in range(n + 1):
        if i == 0:
            i = 1
        if people[i] == 1:
            live.append(i)
    # print(live)
    # print(dead)
    return render_template("index.html", dead=dead, live=live, n=n, m=m, k=k, index=begin)


if __name__ == '__main__':
    app.run(debug=True)
