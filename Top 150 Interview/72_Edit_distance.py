class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        def edit_distance(s1,s2,i,j,memo):
            if len(s2)==j:
                return len(s1)-i
            if len(s1)==i:
                return len(s2)-j
            
            if (i,j) in memo:
                return memo[(i,j)]    
            
            if s1[i]==s2[j]:
                memo[(i,j)]=edit_distance(s1,s2,i+1,j+1,memo)
                return memo[(i,j)]
            else:
                insert_op= 1 + edit_distance(s1,s2,i,j+1,memo)
                delete_op= 1 + edit_distance(s1,s2,i+1,j,memo)
                replace_op= 1 + edit_distance(s1,s2,i+1,j+1,memo)
                
                memo[(i,j)]=min(insert_op,delete_op,replace_op)
                return memo[(i,j)]
            
        return edit_distance(word1,word2,0,0,{})
    
    
    
# Real-World Applications of Edit Distance (Min Insertions, Deletions, Replacements):

# 1. Browser Search Request Typo Handling:
# When a user types a misspelled search query (e.g., "enviroment") into a browser,
# the backend uses edit distance to find the closest valid words or topics and suggests:
# "Did you mean 'environment'?" — then returns results accordingly.

# 2. Search Engine Autocorrect (e.g., Google, Bing):
# Search engines apply edit distance to match misspelled keywords to the correct term.
# For example, a query like "definately good movies" will automatically be corrected to
# "definitely good movies" to fetch more relevant results.

# 3. Google Voice Assistant & ASR (Automatic Speech Recognition):
# Voice inputs often include misheard or phonetically similar words.
# Edit distance helps map the recognized string to the closest real-world commands or names.
# Example: "Set an alram" → corrected to "Set an alarm".

# 4. Plagiarism Checkers:
# Tools like Turnitin or Copyscape use edit distance to detect copied content with slight modifications.
# For example, changing a few words or rearranging sentences still shows similarity using edit distance algorithms.

# 5. DNA/RNA/Protein Sequence Alignment (Bioinformatics):
# Edit distance helps compare two gene or protein sequences to identify mutations, insertions, or deletions.
# Example: Comparing virus genomes to detect variants or evolutionary relationships.

# These diverse applications all rely on the core concept of measuring how similar two sequences are,
# even when they're not identical — enabling smarter responses, corrections, or analyses.
