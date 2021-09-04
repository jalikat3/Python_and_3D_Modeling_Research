using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewShepardBasic : MonoBehaviour
{

    [SerializeField] float thrusterForce;
    [SerializeField] Canvas canvas;
    //[SerializeField] Plane plane;
    float time;
    
    bool thrust = false;


    Rigidbody rb;
    // Start is called before the first frame update
    void Awake()
    {
        rb = GetComponent<Rigidbody>();
  
    }

    private void Update()
    {
        thrust = Input.GetKey(KeyCode.W);
        time += Time.deltaTime;
        Debug.Log(time);
       

    }
    private void FixedUpdate()
    {
        if (thrust)
        {
            rb.AddForce(Vector3.up*thrusterForce);
            thrust = false;
            canvas.gameObject.SetActive(false);
        }
        if (!thrust)
        {
            rb.AddForce(Vector3.down * (thrusterForce / 2));

        }
    }

    // attempt to put the canvas back on after initial thrust
    private void OnCollisionEnter()
    {
        if(rb.gameObject.transform.CompareTag("Ground")&&time>=10.0f)
        {
            canvas.gameObject.SetActive(true);
        }
    }
}
