import json
import os 
from typing import TypedDict
from dotenv import load_dotenv

from openai  import AsyncOpenAI
from langgraph.graph import StateGraph ,START , END
load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPEN_AI_KEY"))

FAKE_SECTION_SUMMARY = (#
        "Cette section couvre la définition des sous-espaces vectoriels, "
        "les critères de sous-espace, et des exemples simples en dimension finie.")

class RouteState(TypedDict):
    question :str
    route :str
    result : str

async def classify_node(state: RouteState) -> dict:
    prompt = (
        f"Contenu de la section actuelle :\n{FAKE_SECTION_SUMMARY}\n\n"
        f"Question de l'étudiant : {state['question']}\n\n"
        "Cette question peut-elle être répondue uniquement à partir du contenu "
        "ci-dessus, ou nécessite-t-elle une recherche plus large dans tout le cours ?"
    )
    completion = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name":"route_decision",
                "schema":{
                    "type":"object",
                    "properties":{
                        "route": {"type": "string", "enum": ["section", "corpus"]}                    },
                    "required":["route"],
                    "additionalProperties":False,
                },
                "strict":True,
            },
        },
        
    )

    decision = json.loads(completion.choices[0].message.content)
    print(f"classify_node: {state['question']!r} -> {decision['route']}")
    return {"route": decision["route"]}

def handle_section(state: RouteState) -> dict:
    return {"result": "Would answer from the current SECTION only."}

def handle_corpus(state: RouteState) -> dict:
    return {"result": "Would run a CORPUS-wide search."}

def route_after_classify(state: RouteState) -> str:
    return state["route"]

graph = StateGraph(RouteState)
graph.add_node("classify_node", classify_node)
graph.add_node("handle_section", handle_section)
graph.add_node("handle_corpus", handle_corpus)

graph.add_edge(START,"classify_node")
graph.add_conditional_edges(
    "classify_node",
    route_after_classify,
    {
        "section":"handle_section","corpus":"handle_corpus"
    }

)
graph.add_edge("handle_section",END)
graph.add_edge("handle_corpus",END)

app =  graph.compile()

async def run_all_questions():
    questions = [
        "Qu'est-ce qu'un sous-espace vectoriel ?",
        "Donne un exemple de sous-espace en dimension 3.",
        "Quel est le théorème spectral pour les matrices symétriques ?",
        "Explique la décomposition en valeurs singulières.",
        "Quels sont les critères pour qu'un sous-ensemble soit un sous-espace ?",
    ]
    
    # Compile the graph once inside the active loop
    compiled_app = graph.compile() 
    
    for q in questions:
        # Await the async execution cleanly within the SAME event loop
        result = await compiled_app.ainvoke({"question": q, "route": "", "result": ""})
        print(f"Question: {q}")
        print(f"Result: {result['result']}\n" + "-"*40)

# 2. Call asyncio.run() ONLY ONCE here
if __name__ == "__main__":
    import asyncio
    asyncio.run(run_all_questions())