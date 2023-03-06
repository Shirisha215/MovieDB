from flask import Flask,request,jsonify,abort
app=Flask(__name__)
@app.route('/api/moviedb',methods=['GET','POST'])
def mymoviedb():
    if request.method=='GET':
        return "Im ALive"
    else:

        
        return jsonify({})
    
if __name__ == '__main__':
    app.run("0.0.0.0",port=8209)