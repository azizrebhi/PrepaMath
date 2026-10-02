import json
import os  
from typing import TypedDict, Annotated
import operator
from dotenv import load_dotenv
from openai import AsyncOpenAI
from langgraph.graph import START, END,StateGraph

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPEN_AI_KEY"))

FAKE_SECTION_SUMMARY = (
        "Cette section couvre la définition des sous-espaces vectoriels, "
            "les critères de sous-espace, et des exemples simples en dimension finie.")

class TutorState(TypedDict):
    question:str
    route:str
    context:str
    answer:str
    history:Annotated[list,operator.add]

async def classify_node(state: TutorState) -> dict:
    prompt=(
 f"Contenu de la section actuelle :\n{FAKE_SECTION_SUMMARY}\n\n"
 f"Question de l'etudiant : {state['question']}\n\n "
 "Cette question peut-elle etre repondue uniquement a partir du contenu "
 "ci-dessus, on necessite-t-elle une recherche plus large dans tous le cours ?"
    )
    completion = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={
            "type":"json_schema",
            "json_schema":{
                "name":"route_decision",
                "schema":{
                    "type":"object",
                    "properties":{"route":{"type":"string","enum":["section","corpus"]}},
                    "required":["route"],
                    "additionalProperties":False,
                },
                "strict":True,

            }

        }
    )
    decision = json.loads(completion.choices[0].message.content)
    print(f"classify_node:{state['question']!r}->{decision['route']}")
    return {"route": decision["route"]}

def handle_section(state: TutorState) -> dict:
    return {"context": FAKE_SECTION_SUMMARY}

def handle_corpus(state:TutorState)->dict : 
    return {"context": "Théorème spectral : toute matrice symétrique réelle est diagonalisable en base orthonormée."}

def route_after_classify(state:TutorState):
    return state["route"]

async def generate_node(state: TutorState) -> dict:
    messages = (
        [{"role": "system", "content": "Tu es un tuteur de mathématiques. Réponds en français, brièvement, en te basant sur le contexte fourni."}]
        + state["history"]
        + [{"role": "user", "content": f"Contexte :\n{state['context']}\n\nQuestion : {state['question']}"}]
    )
    completion = await client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    answer = completion.choices[0].message.content.strip()

    new_turn = [
        {"role": "user", "content": state["question"]},
        {"role": "assistant", "content": answer},
    ]
    return {"answer": answer, "history": new_turn}

graph=StateGraph(TutorState)

graph.add_node("classify",classify_node)
graph.add_node("handle_Section",handle_section)
graph.add_node("handle_Corpus",handle_corpus)
graph.add_node("generate_node", generate_node)


graph.add_edge(START,"classify")
graph.add_conditional_edges(
    "classify",
    route_after_classify,
    {"section":"handle_Section","corpus":"handle_Corpus"}
)
graph.add_edge("handle_Section", "generate_node")
graph.add_edge("handle_Corpus", "generate_node")
graph.add_edge("generate_node", END)

app = graph.compile()

if __name__ == "__main__":
    import asyncio

    async def main():
        state = {"question": "Qu'est-ce qu'un sous-espace vectoriel ?", "route": "", "context": "", "answer": "", "history": []}
        r1 = await app.ainvoke(state)
        print("Turn 1 route:", r1["route"])
        print("Turn 1 answer:", r1["answer"], "\n")

        next_state = {"question": "Donne-moi un exemple de ça.", "route": "", "context": "", "answer": "", "history": r1["history"]}
        r2 = await app.ainvoke(next_state)
        print("Turn 2 route:", r2["route"])
        print("Turn 2 answer:", r2["answer"])
        print("Turn 2 history length:", len(r2["history"]))

        next_state = {"question": "c est auoi le Théorème spectral", "route": "", "context": "", "answer": "", "history": r2["history"]}
        r3 = await app.ainvoke(next_state)
        print("Turn 2 route:", r3["route"])
        print("Turn 2 answer:", r3["answer"])
        print("Turn 2 history length:", len(r3["history"]))

    asyncio.run(main())


