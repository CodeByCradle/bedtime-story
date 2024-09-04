class BedTimeStory(): 
    def __init__(self): 
        self.story_dict = {
            "story_1": "High in the sky, a little star yawned. \"Time to sleep\", it whispered. It twinkled softly, then closed its eyes. The moon smiled, and the star drifted off to dreamland, where all the stars sleep, glowing gently through the night.", 
            "story_2": "A soft breeze whispered through the trees, \"Sleep, little leaves\". The leaves rustled and swayed, feeling cozy and warm. They cuddled up tight on the branches, rocking gently to sleep as the breeze sang them a lullaby.", 
            "story_3": "In a cozy cave, a baby bear yawned. Mama Bear wrapped her in a big, warm hug. \"Goodnight, little bear\", Mama said. The baby bear smiled and closed her eyes, snuggled close, and drifted into sweet dreams."
        }
    
    def get_story_titles(self): 
        return self.story_dict.keys() 
    
    def get_story(self, title):
        return self.story_dict.get(title, "No story is found") 
    
