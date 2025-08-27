import json

file_name = "youtube.txt"


def load_data():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open(file_name, "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print()
    print("*" * 100)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, duration: {video['time']}")
    print()
    print("*" * 100)


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid Index Selected!!")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to deleted: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid Index Selected!!")


def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager | Choose an Option")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid Choice!!")


if __name__ == "__main__":
    main()
