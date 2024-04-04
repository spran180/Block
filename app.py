from flask import Flask, jsonify, request

app = Flask(__name__)

resumes = [
    {
        'id': 1,
        'name': 'John Doe',
        'title': 'Software Developer',
        'skills': ['Python', 'JavaScript', 'HTML', 'CSS'],
        'experience': '5 years',
    },
    {
        'id': 2,
        'name': 'Jane Smith',
        'title': 'UX Designer',
        'skills': ['UI/UX Design', 'Wireframing', 'Prototyping'],
        'experience': '3 years',
    },
    # Add more resumes as needed
]

@app.route('/resumes', methods=['GET'])
def get_resumes():
    return jsonify({'resumes': resumes})

@app.route('/resumes/<int:resume_id>', methods=['GET'])
def get_resume(resume_id):
    resume = next((r for r in resumes if r['id'] == resume_id), None)
    if resume:
        return jsonify({'resume': resume})
    else:
        return jsonify({'error': 'Resume not found'}), 404

@app.route('/resumes', methods=['POST'])
def create_resume():
    new_resume = {
        'id': len(resumes) + 1,
        'name': request.json['name'],
        'title': request.json['title'],
        'skills': request.json['skills'],
        'experience': request.json['experience'],
    }
    resumes.append(new_resume)
    return jsonify({'resume': new_resume}), 201