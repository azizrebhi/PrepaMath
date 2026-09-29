export default function RightPanel() {
  return (
    <div className="flex flex-col h-full text-neutral-100">
      {/* TODO 3: header bar — think of it like the navbar's internal
          layout (flex row, justify-between). Put something like a
          "AI Tutor" label on the left for now. */}
      <div className="flex-shrink-0 flex items-center justify-between border-b border-neutral-800 p-4">
        <span>AI Tutor</span>
        <span className="text-xs text-neutral-500">Status: Active</span>
      </div>

      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {/* TODO 4: message list goes here eventually. Hardcode one or
            two fake message bubbles (plain divs, no styling pressure)
            just to confirm this region scrolls independently of
            LeftPanel when content overflows. */}
        <div className="bg-neutral-900 border border-neutral-800 p-3 rounded">
          Fake message 1: Hello from the AI tutor. This panel should scroll when content grows too tall!
        </div>
        <div className="bg-neutral-900 border border-neutral-800 p-3 rounded">
          Fake message 2: Hello! This is a simple user reply message bubble to fill out the scrolling stream area.
        </div>
        {/* Repeat block to force scrolling for overflow testing if needed */}
        <div className="bg-neutral-900 border border-neutral-800 p-3 rounded opacity-50">
          Fake message 3: Extra message block to test layout boundaries.
        </div>
      </div>

      <div className="flex-shrink-0 border-t border-neutral-800 p-4">
        {/* TODO 5: input bar — a text input + a button, side by side.
            No onClick/state yet, that's the backend-wiring step. */}
        <div className="flex items-center gap-2">
          <input 
            type="text" 
            placeholder="Type your message..." 
            className="flex-1 bg-neutral-900 border border-neutral-800 p-2 rounded outline-none text-sm"
          />
          <button className="bg-neutral-800 border border-neutral-700 px-4 py-2 rounded text-sm hover:bg-neutral-700">
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
