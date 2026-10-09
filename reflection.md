# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|15     | HIGHER Hint       | LOWER Hint      | None                   |
|Enter  | Submits guess     | Does nothing    | None                   |
|NewGame| Creates a new game| New game, ends  | None                   |
|85     | LOWER HINT        | HIGHER Hint     | None

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used the built in Copilot agent for this project.
One example the agent suggested was to refactor the game logic that was present in both app.py and logic_utils.py. This is correct suggestion that the AI made, and I verified that by checking the logic to make sure that it all still works in the game.
One expample of a suggestion I did not accept was a change in better range-aware hints. It is out of scope and is a quality of life change rather than being functional.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided the bug was fixed when I could no longer encounter the bug while playing the game.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran a pytest alongside the starter tests, and they all passed. This shows that the code has been fixed now.
- Did AI help you design or understand any tests? How?
AI designed the custom pytest.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit asks to rerun whenever any changes are made to the code and that will update it. However, it doesn't reset the session state. To do that, I had to refresh the page.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I've never used Git inside of VSCode before, and knowing how to do everything I need to inside of VSCode will be very useful.
- What is one thing you would do differently next time you work with AI on a coding task?
I need to be more specific in my prompts so that it does just what I ask it to rather than try to change everything inside the app.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I've realized how powerful AI can be for debugging broken code. It caught and fixed most of the errors before I could catch them myself. Some bugs were very obvious and easy to catch, but others were a bit more hidden and would have taken me much more time to find them myself.
