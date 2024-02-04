$(document).ready(function () {
  $("#content").summernote({
    tabsize: 2,
    height: 300,
    minHeight: null,
    maxHeight: null,
    focus: true,

    toolbar: [
      ["style", ["style"]],
      ["font", ["bold", "italic", "underline", "clear"]],
      ["fontname", ["fontname"]],
      ["fontsize", ["fontsize"]],
      ["color", ["color"]],
      ["misc", ["undo", "redo", "codeview"]],
      ["para", ["ul", "ol", "paragraph"]],
      ["height", ["height"]],
      ["table", ["table"]],
      ["insert", ["link", "picture", "video"]],
      ["view", ["fullscreen", "codeview", "help"]],
    ],
    styleTags: [
      "p",
      "code",
      "blockquote",
      "pre",
      "h1",
      "h2",
      "h3",
      "h4",
      "h5",
      "h6",
    ],
  });
});
