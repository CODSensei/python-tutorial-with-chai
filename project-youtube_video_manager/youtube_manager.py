import sqlite3

conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor()

cursor.execute(
    """
    create table if not exists videos (
        id integer primary key,
        name text not null,
        time text not null
    )
"""
)


def list_videos():
    cursor.execute("select * from videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("insert into videos(name, time) values(?,?)", (name, time))
    conn.commit()


def update_video(video_id, name, time):
    cursor.execute(
        "update videos set name = ?, time = ? where id = ?", (name, time, video_id)
    )
    conn.commit()


def delete_video(video_id):
    cursor.execute("delete from videos where id = ?", (video_id,))
    conn.commit()


def main():
    while True:
        print("\nYoutube Manager App")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter video id: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter video id: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid Choice!!")

    conn.close()


if __name__ == "__main__":
    main()
