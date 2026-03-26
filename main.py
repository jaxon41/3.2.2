#Activity 3.2.2 Step 7
from post import Post

all_posts_archive = []

# your code here
username = input("enter your username: ")
print(f"Your username is: {username}")
print(f"Welcome to Computogram {username}!")
user_input = input("Type new to add post, remove to delete a post, change user to change your username, print to display all posts, or quit to end the program: ")
while user_input != "quit":
    if user_input == "new":
        post_content = input("What would you like to post? ")
        new_post = Post(username, post_content)
        all_posts_archive.append(new_post)
    elif user_input == "remove":
        try: #A try/except loop is attempting the input, then if the input triggers one of the except it will redirect the code instead, this is to let the input allow errors and lightly break the code instead of failing.
            post_id_to_remove = int(input("Enter the post ID to remove: "))
            for post in all_posts_archive:
                if post.get_post_id() == post_id_to_remove and post.get_user_name() == username:
                    all_posts_archive.remove(post)
                    print(f"Post with ID {post_id_to_remove} removed.")
                    break
            else:
                print("Post not found or you don't own it.")
        except ValueError:
            print("Invalid ID. Please enter a number.")
    elif user_input == "change user":
        username = input("Enter your new username: ")
        print(f"Your username has been changed to: {username}")
    elif user_input == "print":
        if not all_posts_archive:
            print("No posts yet.")
        else:
            for post in all_posts_archive:
                print(f"ID {post.get_post_id()}: {post}")
    else:
        print("Invalid input. Please try again.")
    
    user_input = input("Type new to add post, remove to delete a post, change user to change your username, print to display all posts, or quit to end the program: ")
