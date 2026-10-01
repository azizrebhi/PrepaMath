import os 
from typing import TypedDict,Annotated
from dotenv import load_dotenv
from openai import AsyncOpenAI
import operator
from langgraph.graph import StateGraph, START, END
load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPEN_AI_KEY"))
class chatState(TypedDict):
    question : str
    answer : str
    history: Annotated[list,operator.add]


async def generate_node(state:chatState)-> dict : 
    messages= (
        [{"role": "system", "content": "Tu es un tuteur de mathématiques. Réponds en français, brièvement."}]
        +state["history"]+[{"role":"user","content":state["question"]}]
    )
    completion = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,)
    answer = completion.choices[0].message.content.strip()
    new_turn = [
                {"role": "user", "content": state["question"]},
                {"role": "assistant", "content": answer},]
    return {"answer": answer, "history": new_turn}
graph = StateGraph(chatState)
graph.add_node("generate_node", generate_node)
graph.add_edge(START, "generate_node")
graph.add_edge("generate_node", END)
app = graph.compile()

if __name__=="__main__":
    import asyncio
    async def main():
        state = {"question": "Qu'est-ce qu'un sous-espace vectoriel ?", "answer": "", "history": []}
        result1 = await app.ainvoke(state)
        print("Turn 1 - history length:", len(result1["history"]))
        print("Turn 1 - answer:", result1["answer"], "\n")

        next_state = {"question": "Donne-moi un exemple.", "answer": "", "history": result1["history"]}
        result2 = await app.ainvoke(next_state)
        print("Turn 2 - history length:", len(result2["history"]))
        print("Turn 2 - answer:", result2["answer"])

asyncio.run(main())