class TextPart:
   def __init__(self, id, start, end, text):
      self.id = id
      self.start_pos = start
      self.end_pos = end
      self.original_text = text
      self.obfuscated_text = text
