# Mini-Sports1M

### [Paper](https://cs.stanford.edu/people/karpathy/deepvideo/deepvideo_cvpr2014.pdf) | [Dataset](https://cs.stanford.edu/people/karpathy/deepvideo/) | [github](https://github.com/gtoderici/sports-1m-dataset/)


Sports1M is one of the biggest sports video datasets in the vision community, which contains 487 categories and has been well-annotated. Considering the fact that some of its URLs are no longer available as well as its huge amount (the original version contains over 1 million videos), we construct a mini version of it, which only includes 50 samples per class, 40 for training, and 10 for testing. We released the pre-downloaded mini-Sports1M via [Dropbox](https://www.dropbox.com/scl/fo/6j05er1hlxndt1z9h3t4q/h?dl=0&rlkey=mzk5tlyx87e5gfbi4qcgtmv3e). Please download the split `.tar.gz.part*` files here.

## Download and preprocessing

- Run the following command: 
    ```
    bash prerpocess_mini_sports1m.sh
    ```