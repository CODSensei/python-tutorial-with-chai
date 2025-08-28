def list_videos():
    pass


def add_video(name, time):
    pass


def update_video(video_id, name, time):
    pass


def delete_video(video_id):
    pass


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
