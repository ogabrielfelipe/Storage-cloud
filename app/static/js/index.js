$(document).ready(function () {
    $('#btn_enviaForm').click((event)=>{
        event.preventDefault();
        var form = $("#arquivo").get(); 
        console.log(form)
        form.get().forEach(function (form, i){
            var arquivos = form.files[0];
            console.log(arquivos)
        });
        var data = new FormData(form);
        console.log(data);

        $.ajax({
          type: "POST",
          enctype: "multipart/form-data",
          url: "http://127.0.0.1:5000/arquivos/envia",
          data: data,
          processData: false,
          contentType: false,
          success: function (data) {

            $('<iframe>', {
                src: 'http://127.0.0.1:5000/arquivos/'+data['id_arquivo'],
                id:  'iframeResp',
                frameborder: 0,
                scrolling: 'no',
                width: 800,
                height: 600
            }).appendTo('#content_iframe');

            console.log(data);
          },
          error: function (e) {
            console.log(e);
          },
        });
    });

});
