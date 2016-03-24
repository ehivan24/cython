class Particle{
    public:
        float mass, charge;
        float vel[3], pos[3];
        Particle(float m, float c, float *p, float *v);
        ~Particle();
        float getMass();
        void setMass(float m);
        float getCharge();
        const float *getVel();
        const float *getPos();
        void applyImpulse(float *f, float t);
};