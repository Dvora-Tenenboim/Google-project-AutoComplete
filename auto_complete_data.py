
#@dataclass
class AutoCompleteData:
    def __init__(self, completed_sentence, source_text,file_name, line_in_file, less_score=0):
        self.completed_sentence = completed_sentence
        self.source_text=source_text
        self.offset=self.calculateOffset()
        self.score=self.calculateScore(less_score)
        self.file_name=file_name
        self.line_in_file=line_in_file

    def __repr__(self):
        return "% s (% s % d)" % (self.completed_sentence, self.file_name,self.line_in_file)

    def calculateOffset(self):
        return self.completed_sentence.find(self.source_text)
    def calculateScore(self,less_score):
        return len(self.source_text)*2-less_score

