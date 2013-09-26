import logging
from boto.utils import get_instance_metadata
from boto.sns import SNSConnection
 
class SNSLogHandler(logging.Handler):
    def __init__(self, topic, subject, instance_id=None):
        logging.Handler.__init__(self)
        self.sns_conn = SNSConnection()
        self.topic = topic
        self.subject = subject
        self.instance_id = instance_id
 
    def emit(self, record):
        if self.instance_id is None:
            msg = record.message
        else:
            msg = "[from: %s] %s" % (self.instance_id, record.message)
        self.sns_conn.publish(self.topic, msg,
            subject=self.subject)

class MyClass(object):
    def __init__(self):
        # Set up the logging early here to better catch all errors.
        # Obtain the SNS URN by first creating a new topic in the AWS
        # Management Console: https://console.aws.amazon.com
        self.sns_topic = "arn:aws:sns:us-east-1:118529612345:MyTopic"
        self.sns_subject = "This is my SNS subject."
        self._init_logging()
        """
        Do more initialization stuff 
        """
        self.log.critical("Oh noes!! Something really bad happened!")
 
    def _init_logging(self):
        self.log = logging.getLogger('my_logger')
 
        # Should set the level on the logger itself to DEBUG
        # and let the handlers below do the filtering 
        self.log.setLevel(logging.DEBUG)
 
        # Setting console output to DEBUG for easier debugging
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.log.addHandler(ch)
 
        """
        Assuming that this script is running on an EC2 instance
        we grab the instance ID so it can be included in the SNS
        message for reference.  If you're not running this on EC2,
        remove this rather than trap the exception because the timeout
        is several seconds long.
        """
        instance_id = get_instance_metadata()['instance_id']
        sns = SNSLogHandler(self.sns_topic, self.sns_subject, instance_id)
 
        # We only want critical messages bothering us via AWS SNS
        sns.setLevel(logging.CRITICAL)
        sns.setFormatter(formatter)
        self.log.addHandler(sns)