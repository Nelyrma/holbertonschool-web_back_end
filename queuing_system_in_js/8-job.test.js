import kue from 'kue';
import assert from 'assert';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(function() {
    queue.testMode.enter();
  });
  
  afterEach(function() {
    queue.testMode.clear();
  });
  
  after(function() {
    queue.testMode.exit()
  });

  it('display a error message if jobs is not an array', () => {
    const list = 'Hello world';
    assert.throws(
      () => { createPushNotificationsJobs(list, queue); }, { name: 'Error', message: 'Jobs is not an array'},
    ); 
  });
  it('create two new jobs to the queue', function() {
    const list = [
        {
          phoneNumber: '4153518780',
          message: 'This is the code 1234 to verify your account'
        },
        {
          phoneNumber: '4153518780',
          message: 'This is the code 1234 to verify your account'
        }
    ];
    createPushNotificationsJobs(list, queue);
    assert.equal(queue.testMode.jobs.length, 2);
    assert.equal(queue.testMode.jobs[0].type, 'push_notification_code_3');
    assert.deepStrictEqual(queue.testMode.jobs[0].data, {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    });
  });
  it('check the type of a job', function() {
    const list = [
        {
          phoneNumber: '4153518780',
          message: 'This is the code 1234 to verify your account'
        },
        {
          phoneNumber: '4153518780',
          message: 'This is the code 1234 to verify your account'
        }
    ];
    createPushNotificationsJobs(list, queue);
    assert.equal(queue.testMode.jobs[0].type, 'push_notification_code_3');
  });
  it('check the data of a job', function() {
    const list = [
        {
          phoneNumber: '4153518780',
          message: 'This is the code 1234 to verify your account'
        },
        {
          phoneNumber: '4153518780',
          message: 'This is the code 1234 to verify your account'
        }
    ];
    createPushNotificationsJobs(list, queue);
    assert.deepStrictEqual(queue.testMode.jobs[0].data, {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    });
  });
});