import gradio as gr

def hello(nnn):
    return f"hello {nnn}!"

def main():
    print("Hello from myprojectllm!")
    gr.Interface(
        fn=hello,
        inputs="text",
        outputs="text"
    ).launch()



if __name__ == "__main__":
    main()

