import pymongo
from bson import ObjectId

client = pymongo.MongoClient(
    "mongodb+srv://youtube_manager:yt_mgr@cluster0.tdomqfv.mongodb.net"
)

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)


def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})


def update_video(video_id, name, time):
    video_collection.update_one(
        {"_id": ObjectId(video_id)}, {"$set": {"name": name, "time": time}}
    )


def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


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


if __name__ == "__main__":
    main()
