class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, w1, w2=None):
        if w2 == None:
            return w1.upper()
        return w1 + w2



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
