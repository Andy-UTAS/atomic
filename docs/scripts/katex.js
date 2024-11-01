document$.subscribe(({ body }) => {
    renderMathInElement(body, {
      delimiters: [
        { left: "$$",  right: "$$",  display: true },
        { left: "$",   right: "$",   display: false },
        { left: "\\(", right: "\\)", display: false },
        { left: "\\[", right: "\\]", display: true }
      ],
      macros: {
      expectation: ["\\langle #1 \\rangle", 1]
    }
  })
});
