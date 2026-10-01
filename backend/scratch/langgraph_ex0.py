from typing import TypedDict , Annotated
from langgraph.graph import StateGraph, START, END

class RouteState(TypedDict):
    question:str
    route:str
    result:str

def node_decision(state:RouteState)-> dict :
    is_long=len(state["question"])>50
    result="long"if is_long else "short"
    print(f"decide_node: question is {len(state['question'])} chars -> route={result}")
    return {"route":result}

def node_handle_short(state:RouteState):
     return {"result": "handled short question"}
     
def node_handle_long(state:RouteState):
    return {"result": "handled long question"}

def route_after_decide(state: RouteState) -> str:
    return state["route"]




graph=StateGraph(RouteState)
graph.add_node("decision", node_decision)
graph.add_node("short_node", node_handle_short)
graph.add_node("long_node", node_handle_long)

graph.add_edge(START, "decision")
graph.add_conditional_edges("decision", 
                            route_after_decide,
                            {"short":"short_node","long":"long_node"}
                            )
graph.add_edge("short_node", END)
graph.add_edge("long_node", END)


app = graph.compile()

if __name__ == "__main__":
        import asyncio
        short_result = asyncio.run(app.ainvoke({"question": "What is a vector?", "route": "", "result": ""}))
        print("SHORT case:", short_result)

        long_q = "Explain in detail the difference between a subspace and a hyperplane in finite dimension, with examples."
        long_result = asyncio.run(app.ainvoke({"question": long_q, "route": "", "result": ""}))
        print("LONG case:", long_result)
        