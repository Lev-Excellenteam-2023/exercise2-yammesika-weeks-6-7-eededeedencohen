#-----------------
# צָב שָׁלוּחַ - 7.2
#-----------------

class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}
        
    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id
    
    def read_inbox(self, username, n=None):
        """Read the first n messages in the inbox.

        :param str username: The username of the user.
        :param int n: The number of messages to read.
        :type n: int, optional (default is All user's messages)
        :return: The first n messages in the inbox.
        :rtype: list
        :raises KeyError: if the user does not exist.
        :raises ValueError: if n is negative or larger than the number of messages of the user.
        """
        user_box = self.boxes[username]
        if n is None or n > len(user_box):
            return user_box
        if n < 0:
            raise ValueError("Invalid number of messages to read.")
        return user_box[:n]
    
    def search_inbox(self, username, query):
        """Search the inbox for a query.

        :param str username: The username of the user.
        :param str query: The query to search for.
        :return: All messages that contain the query.
        :rtype: list
        :raises KeyError: if the user does not exist.
        """
        user_box = self.boxes[username]
        return [message for message in user_box if query in message['body']]
    
    

    