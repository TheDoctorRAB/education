function onOpen() {
  var ui = DocumentApp.getUi();
  // Or FormApp or SpreadsheetApp.
  ui.createMenu('Custom Menu')
      .addItem('Insert Date', 'insertDate')
      .addToUi();

}

function insertDate() {
  var cursor = DocumentApp.getActiveDocument().getCursor();
  if (cursor) {
      // Attempt to insert text at the cursor position. If insertion returns null,
      // then the cursor's containing element doesn't allow text insertions.
      var d = new Date();
      var dd = d.getDate();
      dd = pad(dd, 2)
      var mm = d.getMonth() + 1; //Months are zero based
      mm = pad(mm, 2)
      var yyyy = d.getFullYear();
      var date = "rev. " + yyyy+ "." + mm + "." + dd;
      var element = cursor.insertText(date);
      if (element) {
        element.setItalic(true);
        element.setFontSize(10);
        element.setFontFamily('Garamond');
      } else {
        DocumentApp.getUi().alert('Cannot insert text at this cursor location.');
      }
    } else {
      DocumentApp.getUi().alert('Cannot find a cursor in the document.');
  }

}
function pad (str, max) {
  str = str.toString();
  return str.length < max ? pad("0" + str, max) : str;
}
