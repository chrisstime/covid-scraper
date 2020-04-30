jQuery(document).ready(function ($) {

  // make code pretty
  window.prettyPrint && prettyPrint();

  // custom js for cases_in_australia page.
  $('#update-cases').click(function () {
    $('#update-cases-modal').modal('toggle');
  });

  $('#page-refresh').click(function () {
    location.reload();
  });

  $('#council-search').change(
    function () {
      document.getElementById('postcode-search').value = '';
      // Declare variables
      var input, filter, tr, th, td, i, txtValue;
      input = document.getElementById('council-search');
      filter = input.value.toUpperCase();
      th = document.getElementById("paginated-results");
      tr = th.getElementsByTagName('tr');

      // Loop through all list items, and hide those who don't match the search query
      for (i = 1; i < tr.length; i++) {
        td = tr[i].children[6];
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  );

  $('#postcode-search').keyup(
    function () {
      document.getElementById('council-search').selectedIndex = -1;
      // Declare variables
      var input, filter, tr, th, td, i, txtValue;
      input = document.getElementById('postcode-search');
      filter = input.value.toUpperCase();
      th = document.getElementById("paginated-results");
      tr = th.getElementsByTagName('tr');

      // Loop through all list items, and hide those who don't match the search query
      for (i = 1; i < tr.length; i++) {
        td = tr[i].children[2];
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  );

});