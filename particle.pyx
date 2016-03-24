cdef extern from "rectangle_extern.h":
    cppclass _Particle "Particle":
        float mass, charge, vel[3], pos[3]
        _Particle(float m, float c, float *p, float *v)
        float getMass()
        void setMass()
        float getCharge()
        const float *getVel()
        const float *getPos()
        void applyImpulse(float *f, float t)
        
cdef class Particle:
    cdef _Particle *thisptr
    
    cdef __cinit__(self, m, c, float[::1] p, float[::1]v ):
        if p.shape[0] != 3 or v.shape[0] != 3:
            raise ValueError("...")
        self.thisptr = new _Particle(a, c, &p[0], &v[0])
        
        def __dealloc__(self):
            del self.thisptr
        def applyImpulse(self, float[::1] p, float[::1]v )
            self.thisptr.applyImpulse(&v[0],t)

        property mass:
            def __get__(self):
                return self.thisptr.getMass()
            
            def __set__(self, m):
                self.thisptr.setMass(m)